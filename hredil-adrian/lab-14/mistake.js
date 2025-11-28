class UserService {
  createUser(data) {
    if (!data.email.includes("@")) {
      throw new Error("Invalid email");
    }
    console.log("Saving user to DB:", data);
    console.log("Sending email to:", data.email);
  }
}
const service = new UserService();
service.createUser({ email: "test@gmail.com" });
