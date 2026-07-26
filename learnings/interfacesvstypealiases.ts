interface User {
    id : number;
    name :string;
    readonly createdAt: Date;
    email?: string;
}

type UserType = {
    id : number;
    name :string;
};