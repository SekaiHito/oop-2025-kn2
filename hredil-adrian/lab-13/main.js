class Subject {
  constructor() {
    this.observers = []
  }
  toSubs(fn) {
    this.observers.push(fn)
  }
  toAlert(data) {
    this.observers.forEach(fn => fn(data))
  }
}

const subject = new Subject()

subject.toSubs((data) => {
  console.log("value:", data)
})

const input = document.getElementById("textInput")

input.addEventListener("input", (event) => {
  const value = event.target.value
  subject.toAlert(value)
})