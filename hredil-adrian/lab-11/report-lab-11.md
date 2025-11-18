# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №11**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему** 

**Патерн SingleTone**

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: ст. викладач Назар Заплатинський

### Львів 2025

**Мета роботи - Реалізувати патерн  SingleTone**


## Хід роботи

### Коли викликається Singletone.getInstance(), створюється або повертається 
### вже існуючий єдиний екземпляр класу, зберігаючи його у Singletone.instance
```js 

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
```

## Висновок:

 ### В ході виконання лабораторної роботи, мною було реалізован патерн SingleTone, який птрібний для того щоб ### у програмі існував лише один екземпляр певного класу, і щоб до нього можна було глобально звертись
