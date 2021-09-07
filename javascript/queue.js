class Queue {
    constructor() {
      this.items = [];
    }
  
    size() {
      return this.items.length;
    }
  
    enqueue(element) {
      this.items.push(element);
    }
  
    dequeue() {
      if (this.isEmpty()) throw Error("Underflow");
  
      return this.items.shift();
    }
  
    front() {
      if (this.isEmpty()) throw Error("No elements in  the queue");
  
      return this.items[0];
    }
  
    isEmpty() {
      return this.items.length === 0;
    }
  
    iterate(callback = null) {
      if (callback === null) {
        let str = "";
        for (let i of this.items) {
          str += i + " ";
        }
        str.trim();
        return str;
      }
  
      const iterated = [];
      for (let i of this.items) {
        iterated.push(callback(i));
      }
  
      return iterated;
    }
  }
  
  let arr = [10, 20, 30, 40, 50];
  let queue = new Queue();
  
  console.log("Empty size:", queue.size()); 
  
  console.log("Is empty?", queue.isEmpty()); 
  
  try {
    console.log(queue.dequeue()); 
  } catch (err) {
    console.error("Error for attemtping to dequeue empty queue:", err.message);
  }
  
  // Add items in the queue
  for (let i of arr) {
    queue.enqueue(i);
  }
  
  console.log("Added values:", queue.iterate()); 
  
  console.log("Front:", queue.front()); 
  console.log("Dequeue:", queue.dequeue()); 
  console.log("New Front:", queue.front());
  
 