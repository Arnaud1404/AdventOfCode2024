// Part 1
import * as fs from 'fs';

fs.readFile('./Day1/input.txt', (err, data) => {
    // data contains all the files' data
    if (err) throw err;
    const nums = data.toString().split('\n');

    console.log(nums);
    const n = nums.length;
    const list1: number[] = [];
    const list2: number[] = [];
    for(let i = 0; i < n;i++){
        let row:string[] = nums[i].split('   ');
        let a = Number(row[0]);
        let b = Number(row[1]);
        list1.push(a); list2.push(b);
    }
    list1.sort();
    list2.sort();
    let result = 0;
    for(let i = 0; i < n;i++){
        result += Math.abs(list1[i] - list2[i])
    }
    console.log(result)
});

// Part 2

// HashMap implementation
interface Count{
    [key:number]:number
}

fs.readFile('./Day1/input.txt', (err, data) => {
    // data contains all the files' data
    if (err) throw err;
    const nums = data.toString().split('\n');

    // console.log(nums);
    const n = nums.length;
    const list1: number[] = [];
    const list2: number[] = [];
    for(let i = 0; i < n;i++){
        let row:string[] = nums[i].split('   ');
        let a = Number(row[0]);
        let b = Number(row[1]);
        list1.push(a); list2.push(b);
    }

    const count:Count ={}

    list2.forEach(key => {
        // 0 if undefined
        count[key] = (count[key] || 0) + 1;
    })
    let result = 0;
    list1.forEach(key => {
        // 0 if undefined
        result = result + key * (count[key] || 0)
    })
    console.log(result)
});

