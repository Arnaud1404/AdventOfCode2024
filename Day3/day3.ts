import * as fs from 'fs';

function isInteger(value:string){
    // true if value is indeed an integer
    return Number.isInteger(Number(value))
}

function evaluate(input:string, start:number, end:number):number{
    console.assert(start < end, 'start should be less than end')
    console.assert(end <= input.length, 'end should be within input length')
    // i = reading head
    let i = start
    let result = 0
    while(i < input.length && i < end){
        i = input.indexOf("mul(", i)
        if(i === -1 || i >= end) break;
        i = i + "mul(".length
        let num_length = 0
        let arg1: string = "", arg2: string = ""
        while(i < end && isInteger(input[i]) && num_length <= 3){
            arg1 = arg1 + input[i]
            i++
            num_length++
        }
        if(i < end && input[i] === ","){
            i++
            num_length = 0
            while(i < end && isInteger(input[i]) && num_length <= 3){
                arg2 = arg2 + input[i]
                i++
                num_length++
            }
        }
        if(i < end && input[i] === ")"){
            const num1 = parseInt(arg1);
            const num2 = parseInt(arg2);
            if (!isNaN(num1) && !isNaN(num2)) {
                result = result + num1 * num2;
            }
        }
        i++
    }
    return result
}

fs.readFile('./Day3/input.txt', (err, data) => {
    if (err) throw err
    let input = data.toString()
    console.log("Result 1: %d\n", evaluate(input, 0, input.length))
    let enabled = true;
    let i = 0, result = 0, end = input.length -1;
    while(i < input.length - 1){
        end = enabled ? input.indexOf("don't()", i) : input.indexOf("do()", i)
        if(end !== -1){ // Found an instruction
            if(enabled) result = result + evaluate(input, i, end);
            enabled = !enabled;
        } else { // No instrcution found
            end = input.length;
            if(enabled) result = result + evaluate(input, i, end);
        }
        i = end + 1;
    }
    console.log("Result 2: %d\n", result)
})