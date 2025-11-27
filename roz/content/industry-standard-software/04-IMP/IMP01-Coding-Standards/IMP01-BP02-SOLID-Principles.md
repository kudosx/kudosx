# IMP01-BP02: SOLID Principles

5 nguyên tắc thiết kế hướng đối tượng.

## S - Single Responsibility Principle

> Một class chỉ nên có một lý do để thay đổi

```typescript
// ❌ Bad: Class does too many things
class User {
  saveToDatabase() { }
  sendEmail() { }
  generateReport() { }
}

// ✅ Good: Separated responsibilities
class User {
  constructor(public name: string, public email: string) {}
}

class UserRepository {
  save(user: User) { }
}

class EmailService {
  send(to: string, subject: string, body: string) { }
}
```

## O - Open/Closed Principle

> Open for extension, closed for modification

```typescript
// ❌ Bad: Must modify class to add new payment type
class PaymentProcessor {
  process(type: string, amount: number) {
    if (type === 'credit') { /* ... */ }
    else if (type === 'paypal') { /* ... */ }
    // Must add new else if for each payment type
  }
}

// ✅ Good: Extend through interface
interface PaymentMethod {
  process(amount: number): Promise<void>;
}

class CreditCardPayment implements PaymentMethod {
  async process(amount: number) { /* ... */ }
}

class PayPalPayment implements PaymentMethod {
  async process(amount: number) { /* ... */ }
}

class PaymentProcessor {
  process(method: PaymentMethod, amount: number) {
    return method.process(amount);
  }
}
```

## L - Liskov Substitution Principle

> Subclass phải thay thế được superclass mà không làm thay đổi behavior

```typescript
// ❌ Bad: Square breaks Rectangle behavior
class Rectangle {
  setWidth(w: number) { this.width = w; }
  setHeight(h: number) { this.height = h; }
}

class Square extends Rectangle {
  setWidth(w: number) { this.width = this.height = w; } // Breaks LSP
  setHeight(h: number) { this.width = this.height = h; }
}

// ✅ Good: Use composition or separate hierarchies
interface Shape {
  area(): number;
}

class Rectangle implements Shape {
  constructor(private width: number, private height: number) {}
  area() { return this.width * this.height; }
}

class Square implements Shape {
  constructor(private side: number) {}
  area() { return this.side * this.side; }
}
```

## I - Interface Segregation Principle

> Clients should not depend on interfaces they don't use

```typescript
// ❌ Bad: Fat interface
interface Worker {
  work(): void;
  eat(): void;
  sleep(): void;
}

class Robot implements Worker {
  work() { /* ... */ }
  eat() { throw new Error('Robots cannot eat'); } // Forced to implement
  sleep() { throw new Error('Robots cannot sleep'); }
}

// ✅ Good: Segregated interfaces
interface Workable {
  work(): void;
}

interface Eatable {
  eat(): void;
}

interface Sleepable {
  sleep(): void;
}

class Human implements Workable, Eatable, Sleepable {
  work() { }
  eat() { }
  sleep() { }
}

class Robot implements Workable {
  work() { }
}
```

## D - Dependency Inversion Principle

> Depend on abstractions, not concretions

```typescript
// ❌ Bad: High-level module depends on low-level module
class MySQLDatabase {
  query(sql: string) { /* ... */ }
}

class UserRepository {
  private db = new MySQLDatabase(); // Direct dependency

  findById(id: string) {
    return this.db.query(`SELECT * FROM users WHERE id = ${id}`);
  }
}

// ✅ Good: Depend on abstraction
interface Database {
  query(sql: string): Promise<any>;
}

class UserRepository {
  constructor(private db: Database) {} // Injected dependency

  findById(id: string) {
    return this.db.query(`SELECT * FROM users WHERE id = ${id}`);
  }
}

// Can use any database implementation
const mysqlRepo = new UserRepository(new MySQLDatabase());
const postgresRepo = new UserRepository(new PostgresDatabase());
```

## Summary

| Principle | Key Point |
|-----------|-----------|
| **S**ingle Responsibility | One class = one job |
| **O**pen/Closed | Extend, don't modify |
| **L**iskov Substitution | Subtype must be substitutable |
| **I**nterface Segregation | Small, focused interfaces |
| **D**ependency Inversion | Depend on abstractions |

## Checklist

- [ ] Classes have single responsibility
- [ ] New features via extension, not modification
- [ ] Subtypes are substitutable for base types
- [ ] Interfaces are focused and minimal
- [ ] Dependencies are injected
