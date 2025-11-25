class UserValidator {
  static validate(data) {
    if (!data.email.includes("@")) {
      throw new Error("Invalid email");
    }
  }
}

class UserRepository {
  save(data) {
    console.log("Saving user to DB:", data);
  }
}

class EmailService {
  send(email) {
    console.log("Sending email to:", email);
  }x  
}

class UserService {
  constructor(repository, emailService) {
    this.repository = repository;
    this.emailService = emailService;
  }

  createUser(data) {
    UserValidator.validate(data);
    this.repository.save(data);
    this.emailService.send(data.email);
  }
}

const repo = new UserRepository();
const mailer = new EmailService();
const userService = new UserService(repo, mailer);

userService.createUser({ email: "test@gmail.com" });