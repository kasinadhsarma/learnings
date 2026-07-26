interface User {
    id: number;
    name: string;
    email: string;
}
type UserPreview = Pick<User, "id" | "name">;
type UserWithoutEmail = Omit<User, "email">;
type PartialUser = Partial<User>;
type UserMap = Record< number, User>;
function getSampleUser(): User {
    return {
        id: 1,
        name: "John Doe",
        email: "kasinadhsarma@gmail.com"
    };
}   