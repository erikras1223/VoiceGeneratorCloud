export class Queue {
    private elements: any[];
    constructor(elements?: any[]){
        this.elements = elements ? elements : [];
    }
    push(e: any, hasPriority = false): void {
        if(!hasPriority){
            this.elements.push(e);
        }else {
            this.elements.splice(0,0,e);
        }
        
    }
    pop(): any{
        return this.elements.shift();
    }
    isEmpty() : boolean {
        return this.elements.length === 0;
    }
    getLength(): number {
        return this.elements.length;
    }
    peek(): any {
        return !this.isEmpty() ? this.elements[0] : undefined;
    }
}