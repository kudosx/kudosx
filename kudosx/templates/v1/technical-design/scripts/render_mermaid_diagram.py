#!/usr/bin/env python3
"""
Render Mermaid diagrams from markdown files to PNG/SVG images.

Usage:
    uv run render_mermaid_diagram.py <input_file> [--output <output_file>] [--format png|svg]

Requirements:
    - mermaid-py: uv add mermaid-py
"""

import argparse
import base64
import re
import sys
import urllib.request
from pathlib import Path


def extract_mermaid_blocks(markdown_content: str) -> list[str]:
    """Extract all mermaid code blocks from markdown content."""
    pattern = r'```mermaid\n(.*?)```'
    matches = re.findall(pattern, markdown_content, re.DOTALL)
    return matches


def render_mermaid_ink(mermaid_code: str, output_path: str, output_format: str = "png") -> bool:
    """
    Render mermaid code to an image file using mermaid.ink service.

    Args:
        mermaid_code: The mermaid diagram code
        output_path: Path to save the output image
        output_format: Output format (png, svg)

    Returns:
        True if successful, False otherwise
    """
    try:
        # Encode the mermaid code for the URL
        encoded = base64.urlsafe_b64encode(mermaid_code.encode('utf-8')).decode('ascii')

        # Build the mermaid.ink URL
        if output_format == "svg":
            url = f"https://mermaid.ink/svg/{encoded}"
            expected_content_type = "image/svg+xml"
        else:
            url = f"https://mermaid.ink/img/{encoded}"
            expected_content_type = "image/png"

        # Download the image
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Mermaid Renderer)'}
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            # Read the response data first
            image_data = response.read()

            # Validate content type
            content_type = response.headers.get('Content-Type', '')

            # Check if we got the expected image format
            if not content_type.startswith(('image/', 'application/octet-stream')):
                print(f"Error: Received unexpected content type: {content_type}", file=sys.stderr)
                print("The service may have returned an error page instead of an image.", file=sys.stderr)
                # Check if we got HTML
                if image_data.startswith(b'<!DOCTYPE') or image_data.startswith(b'<html'):
                    print("Received HTML content instead of image. First 200 chars:", file=sys.stderr)
                    print(image_data[:200].decode('utf-8', errors='replace'), file=sys.stderr)
                return False

            # Warn if content type doesn't match expected (but continue if it's still an image)
            # Note: mermaid.ink may return image/jpeg for PNG requests, which is acceptable
            if expected_content_type not in content_type and content_type != 'application/octet-stream' and not content_type.startswith('image/'):
                print(f"Warning: Expected {expected_content_type} but got {content_type}", file=sys.stderr)

        # Additional validation: check if the data looks like an image
        if len(image_data) < 100:
            print(f"Error: Response too small to be a valid image ({len(image_data)} bytes)", file=sys.stderr)
            return False

        # Validate image format - be flexible as mermaid.ink may return different formats
        if output_format == "png":
            # Accept PNG or JPEG (mermaid.ink sometimes returns JPEG)
            is_png = image_data.startswith(b'\x89PNG')
            is_jpeg = image_data.startswith(b'\xff\xd8\xff')
            if not (is_png or is_jpeg):
                print("Error: Data does not appear to be a valid PNG or JPEG file", file=sys.stderr)
                print(f"First 16 bytes: {image_data[:16]}", file=sys.stderr)
                return False

        # Check SVG (should start with < or whitespace then <)
        if output_format == "svg":
            stripped = image_data.lstrip()
            if not (stripped.startswith(b'<svg') or stripped.startswith(b'<?xml')):
                print("Error: Data does not appear to be a valid SVG file", file=sys.stderr)
                print(f"First 50 bytes: {image_data[:50]}", file=sys.stderr)
                return False

        # Save to file
        Path(output_path).write_bytes(image_data)
        print(f"Successfully rendered diagram to: {output_path}")
        return True

    except urllib.error.HTTPError as e:
        print(f"Error from mermaid.ink service: {e.code} {e.reason}", file=sys.stderr)
        return False
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error rendering diagram: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Render Mermaid diagrams from markdown files'
    )
    parser.add_argument(
        'input_file',
        help='Path to the markdown file containing mermaid diagram(s)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: same as input with .png extension)'
    )
    parser.add_argument(
        '-f', '--format',
        choices=['png', 'svg'],
        default='png',
        help='Output format (default: png)'
    )
    parser.add_argument(
        '-a', '--all',
        action='store_true',
        help='Render all mermaid blocks (adds index suffix to output filename)'
    )

    args = parser.parse_args()

    # Read input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: File not found: {args.input_file}", file=sys.stderr)
        sys.exit(1)

    content = input_path.read_text(encoding='utf-8')

    # Extract mermaid blocks
    mermaid_blocks = extract_mermaid_blocks(content)

    if not mermaid_blocks:
        print("No mermaid diagrams found in the file.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(mermaid_blocks)} mermaid diagram(s)")

    # Determine output path
    if args.output:
        output_base = Path(args.output)
    else:
        output_base = input_path.with_suffix(f'.{args.format}')

    # Render diagrams
    success_count = 0

    if args.all or len(mermaid_blocks) == 1:
        for i, block in enumerate(mermaid_blocks):
            if len(mermaid_blocks) > 1:
                output_path = output_base.parent / f"{output_base.stem}_{i+1}{output_base.suffix}"
            else:
                output_path = output_base

            if render_mermaid_ink(block, str(output_path), args.format):
                success_count += 1
    else:
        # Only render the first block if --all not specified
        print("Multiple diagrams found. Use --all to render all, or only first will be rendered.")
        if render_mermaid_ink(mermaid_blocks[0], str(output_base), args.format):
            success_count += 1

    print(f"\nRendered {success_count}/{len(mermaid_blocks) if args.all else 1} diagram(s)")
    sys.exit(0 if success_count > 0 else 1)


if __name__ == '__main__':
    main()
