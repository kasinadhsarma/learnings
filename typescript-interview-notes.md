
# TypeScript Interview Prep Notes

## 1. TypeScript Basics

### What is TypeScript?
A statically typed superset of JavaScript that compiles to plain JS. Adds:
- Static type checking (caught at compile time, not runtime)
- Interfaces, enums, generics, decorators
- Better tooling (autocomplete, refactoring, inline docs)

### Basic Types
```ts
let id: number = 5;
let name: string = "John";
let isActive: boolean = true;
let list: number[] = [1, 2, 3];
let tuple: [string, number] = ["age", 25];
let anything: any = "avoid this";
let notSure: unknown = 4; // safer than any, needs narrowing
let empty: void = undefined; // fn returns nothing
let nothing: null = null;
let notDefined: undefined = undefined;
let fail: never = (() => { throw new Error(); })(); // never returns
```

### `any` vs `unknown` vs `never`
- `any`: opts out of type checking entirely. Avoid — defeats the purpose of TS.
- `unknown`: type-safe counterpart of `any`. Must narrow (typeof/instanceof) before use.
- `never`: represents values that never occur (function always throws, infinite loop, exhaustive switch default).

```ts
function fail(msg: string): never {
  throw new Error(msg);
}

function assertUnreachable(x: never): never {
  throw new Error("Unexpected value");
}
```

---

## 2. Interfaces vs Type Aliases

```ts
interface User {
  id: number;
  name: string;
  readonly createdAt: Date;
  email?: string; // optional
}

type UserType = {
  id: number;
  name: string;
};
```

| Feature | `interface` | `type` |
|---|---|---|
| Extending | `extends` | `&` intersection |
| Declaration merging | Yes (auto-merges same-name) | No |
| Union/Intersection types | No | Yes |
| Primitives/tuples/unions | No | Yes |
| Use for objects/classes | Preferred | Works too |

**Common answer:** Use `interface` for object shapes meant to be extended/implemented (esp. public API), use `type` for unions, tuples, mapped/conditional types.

---

## 3. Generics

```ts
function identity<T>(arg: T): T {
  return arg;
}

interface Box<T> {
  value: T;
}

// Generic constraints
function getLength<T extends { length: number }>(arg: T): number {
  return arg.length;
}

// Multiple type params
function merge<T, U>(a: T, b: U): T & U {
  return { ...a, ...b };
}

// Generic class
class Stack<T> {
  private items: T[] = [];
  push(item: T) { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
}
```
**Why generics?** Reusability with type safety — avoids duplicating code for each type while keeping strong typing (better than `any`).

---

## 4. Union & Intersection Types

```ts
type Status = "success" | "error" | "loading"; // union
type Admin = User & { permissions: string[] }; // intersection

function printId(id: string | number) {
  if (typeof id === "string") {
    console.log(id.toUpperCase()); // narrowed to string
  } else {
    console.log(id.toFixed(2)); // narrowed to number
  }
}
```

### Discriminated Unions (very common interview topic)
```ts
interface Circle {
  kind: "circle";
  radius: number;
}
interface Square {
  kind: "square";
  side: number;
}
type Shape = Circle | Square;

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle": return Math.PI * shape.radius ** 2;
    case "square": return shape.side ** 2;
  }
}
```

---

## 5. Type Narrowing

```ts
// typeof
if (typeof x === "string") { ... }

// instanceof
if (error instanceof Error) { ... }

// in operator
if ("swim" in animal) { ... }

// custom type guards
function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}

// truthiness narrowing
if (value) { ... }
```

---

## 6. Utility Types (memorize these — asked constantly)

```ts
Partial<T>       // all props optional
Required<T>      // all props required
Readonly<T>      // all props readonly
Record<K, T>     // object with keys K and values T
Pick<T, K>       // subset of props
Omit<T, K>       // exclude props
Exclude<T, U>    // exclude types from union
Extract<T, U>    // extract types from union
NonNullable<T>   // remove null/undefined
ReturnType<T>    // return type of a function
Parameters<T>    // tuple of function's param types
InstanceType<T>  // instance type of a class constructor
Awaited<T>       // unwrap Promise type
```

```ts
interface User {
  id: number;
  name: string;
  email: string;
}

type UserPreview = Pick<User, "id" | "name">;
type UserWithoutEmail = Omit<User, "email">;
type PartialUser = Partial<User>;
type UserMap = Record<number, User>;

function getUser(): User { ... }
type UserReturn = ReturnType<typeof getUser>; // User
```

---

## 7. Mapped & Conditional Types

```ts
// Mapped type
type Readonly2<T> = {
  readonly [K in keyof T]: T[K];
};

type Optional<T> = {
  [K in keyof T]?: T[K];
};

// Key remapping (TS 4.1+)
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

// Conditional types
type IsString<T> = T extends string ? true : false;

// infer keyword
type ElementType<T> = T extends (infer U)[] ? U : T;
type Awaited2<T> = T extends Promise<infer U> ? U : T;
```

---

## 8. `keyof`, `typeof`, indexed access

```ts
interface Person {
  name: string;
  age: number;
}

type PersonKeys = keyof Person; // "name" | "age"

const person = { name: "Sam", age: 30 };
type PersonType = typeof person; // { name: string; age: number }

type NameType = Person["name"]; // string
type ValueType = Person[keyof Person]; // string | number
```

---

## 9. Enums

```ts
enum Direction {
  Up,    // 0
  Down,  // 1
  Left,  // 2
  Right, // 3
}

enum Status {
  Active = "ACTIVE",
  Inactive = "INACTIVE",
}

const enum Color { Red, Green, Blue } // inlined at compile time, no object generated
```
**Interview note:** Prefer union of string literals (`type Status = "active" | "inactive"`) over enums in many modern codebases — no runtime footprint, better tree-shaking. Know the tradeoff.

---

## 10. Classes & OOP

```ts
class Animal {
  private name: string;
  protected age: number;
  public readonly species: string;

  constructor(name: string, age: number, species: string) {
    this.name = name;
    this.age = age;
    this.species = species;
  }

  // shorthand property declaration
  // constructor(private name: string, protected age: number) {}

  speak(): string {
    return `${this.name} makes a sound.`;
  }
}

abstract class Shape {
  abstract area(): number;
  describe(): string {
    return `Area is ${this.area()}`;
  }
}

interface Flyable {
  fly(): void;
}

class Bird extends Animal implements Flyable {
  fly(): void {
    console.log("Flying");
  }
}
```

- `private`: only within the class
- `protected`: class + subclasses
- `public`: default, everywhere
- `readonly`: can't reassign after init
- `abstract`: must be implemented by subclass, can't instantiate directly

---

## 11. Function Types & Overloads

```ts
type AddFn = (a: number, b: number) => number;
const add: AddFn = (a, b) => a + b;

// Overloads
function combine(a: string, b: string): string;
function combine(a: number, b: number): number;
function combine(a: any, b: any): any {
  return a + b;
}

// Optional & default params
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}`;
}

// Rest params
function sum(...nums: number[]): number {
  return nums.reduce((a, b) => a + b, 0);
}
```

---

## 12. `strict` mode flags (know what each does)

- `strictNullChecks`: `null`/`undefined` not assignable to other types unless explicit
- `noImplicitAny`: errors on implicit `any`
- `strictFunctionTypes`: stricter checking of function type parameters
- `strictPropertyInitialization`: class props must be initialized
- `noUncheckedIndexedAccess`: indexed access returns `T | undefined`

`"strict": true` in tsconfig enables all of the above — best practice for real projects.

---

## 13. Type Assertions

```ts
const el = document.getElementById("app") as HTMLElement;
const el2 = <HTMLElement>document.getElementById("app"); // not usable in .tsx

// non-null assertion
const value = maybeNull!;

// const assertion
const point = { x: 1, y: 2 } as const; // readonly, literal types
```
**Note:** assertions don't change runtime behavior — they only tell the compiler "trust me." Misuse can cause runtime bugs.

---

## 14. Modules & Namespaces

```ts
// export
export interface Config { ... }
export default class App { ... }

// import
import App, { Config } from "./app";
import * as utils from "./utils";

// dynamic import
const module = await import("./module");
```

---

## 15. Declaration Files (`.d.ts`)

```ts
// global.d.ts
declare module "my-untyped-lib" {
  export function doSomething(x: number): string;
}

declare global {
  interface Window {
    myGlobal: string;
  }
}
```
Used to type JS libraries without types (`@types/*` packages come from DefinitelyTyped).

---

## 16. Common Interview Questions & Answers

**Q: Difference between `interface` and `type`?**
→ See section 2. Key point: interfaces support declaration merging, types support unions.

**Q: What is structural typing (duck typing) in TS?**
→ TS compares shape, not name. Two unrelated types with the same structure are compatible.
```ts
interface Point { x: number; y: number; }
function log(p: Point) { console.log(p); }
log({ x: 1, y: 2, z: 3 }); // OK (extra prop allowed via variable, not object literal)
```

**Q: What is excess property checking?**
→ Object literals assigned directly get checked strictly for extra properties; assigning via a variable does not.
```ts
log({ x: 1, y: 2, z: 3 }); // may error: object literal only
const p = { x: 1, y: 2, z: 3 };
log(p); // OK
```

**Q: Covariance/contravariance? (senior-level question)**
→ Function parameters are checked contravariantly under `strictFunctionTypes`, return types covariantly. Basically: a function expecting a broader param type can be used where a narrower one is expected.

**Q: How does TS handle `null`/`undefined`?**
→ With `strictNullChecks` on, they're distinct types and must be handled explicitly (optional chaining `?.`, nullish coalescing `??`).

**Q: What's the difference between `Object`, `object`, and `{}`?**
→ `Object` = anything with Object.prototype methods (almost anything). `object` = non-primitive. `{}` = anything except `null`/`undefined` (very loose, avoid).

**Q: What does `as const` do?**
→ Makes literal types instead of widened types, and makes properties readonly. Useful for tuples and literal unions.

**Q: Explain `infer`.**
→ Used inside conditional types to extract/capture a type for reuse. See `ElementType<T>` example above.

**Q: How do you type a React component / props?** (if role is frontend)
```ts
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}
const Button: React.FC<ButtonProps> = ({ label, onClick, disabled }) => (
  <button onClick={onClick} disabled={disabled}>{label}</button>
);
```

**Q: Difference between `const enum` and `enum`?**
→ `const enum` is fully inlined at compile time (no JS object emitted); regular `enum` generates a runtime object. `const enum` can't be used with isolatedModules/babel-only pipelines.

**Q: How do you handle typing an async function?**
```ts
async function fetchUser(id: number): Promise<User> {
  const res = await fetch(`/users/${id}`);
  return res.json();
}
```

---

## 17. Practical Coding Exercises to Practice

1. Implement `Pick`, `Omit`, `Partial` from scratch using mapped types.
```ts
type MyPick<T, K extends keyof T> = { [P in K]: T[P] };
type MyPartial<T> = { [P in keyof T]?: T[P] };
type MyOmit<T, K extends keyof any> = MyPick<T, Exclude<keyof T, K>>;
```

2. Write a generic `Result<T, E>` type (like Rust) for error handling.
```ts
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  if (b === 0) return { ok: false, error: "Division by zero" };
  return { ok: true, value: a / b };
}
```

3. Write a `DeepReadonly<T>` recursive mapped type.
```ts
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};
```

4. Implement a type-safe event emitter with generics.
```ts
type EventMap = Record<string, any[]>;

class TypedEmitter<T extends EventMap> {
  private handlers: { [K in keyof T]?: ((...args: T[K]) => void)[] } = {};

  on<K extends keyof T>(event: K, handler: (...args: T[K]) => void) {
    (this.handlers[event] ??= []).push(handler);
  }

  emit<K extends keyof T>(event: K, ...args: T[K]) {
    this.handlers[event]?.forEach((h) => h(...args));
  }
}
```

---

## 18. Quick Cheat Sheet Summary

| Concept | Key takeaway |
|---|---|
| `any` vs `unknown` | `unknown` forces narrowing before use |
| `interface` vs `type` | interfaces merge & extend; types do unions |
| Generics | reusable + type-safe code |
| Discriminated unions | best pattern for modeling variant data |
| Utility types | know `Partial`, `Pick`, `Omit`, `Record`, `ReturnType` cold |
| `infer` | extract types inside conditional types |
| Structural typing | shape matters, not declared name |
| `strictNullChecks` | forces explicit null/undefined handling |
| `as const` | literal + readonly narrowing |

---

## 19. Things to Review Right Before an Interview
- Be ready to write a discriminated union + exhaustive switch from scratch on a whiteboard.
- Be ready to implement 1-2 utility types manually (Pick/Omit/Partial).
- Explain the difference between compile-time types and runtime JS (types erase at compile time — no runtime type info).
- Know how generics interact with constraints (`extends`).
- Be able to explain why `any` is discouraged and what to use instead.
