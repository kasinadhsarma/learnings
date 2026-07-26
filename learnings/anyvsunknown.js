function failWith(msg) {
    throw new Error(msg);
}
function assertUnreachable(x) {
    throw new Error("Didn't expect to get here");
}
