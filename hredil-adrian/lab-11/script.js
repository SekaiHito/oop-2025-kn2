class Singletone {
    static instance;
        constructor () {
        if (!Singletone.instance) {
            Singletone.instance = this;
        }
        return Singletone.instance;
    }

    

        static getInstance() {
        if (!Singletone.instance) {
            Singletone.instance = new Singletone();
        }
        return Singletone.instance;
    }
}

const obj1 = Singletone.getInstance();
const obj2 = Singletone.getInstance();

console.log(obj1 === obj2); 


    
    
