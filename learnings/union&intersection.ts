type Status = "sucess" | "error" | "loading";
type UserProfile = { name: string; email: string };
type Admin = UserProfile & { permissions: string[] };
function printId(id: string | number) {
    if (typeof id === "string") {
        console.log(id.toUpperCase());
    }
    else {
        console.log(id.toFixed(2));
    }
}
