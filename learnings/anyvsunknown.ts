function failWith(msg:string): never {
    throw new Error(msg);
}
function assertUnreachable(x: never): never {
    throw new Error("Didn't expect to get here");
}