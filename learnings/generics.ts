function identity<T>(arg: T): T {
    return arg;
}
interface Box<T> {
    value: T;
}

function getLength<T extends { length: number }>(arg: T): number {
    return arg.length;
}

function merge<T, U>(obj1: T, obj2: U): T & U {
    return {...obj1, ...obj2};
}

