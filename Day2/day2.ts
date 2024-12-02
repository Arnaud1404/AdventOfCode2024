// Part 1

// JAVASCRIPT import fs from 'fs';
// TYPESCRIPT
import * as fs from 'fs';

function check_report(report:string): boolean{
    const levels = report.split(" ");
    let increasing = 0
    // 0 = Not set, 1 = increasing, -1 = decreasing
    for(let i = 0; i < levels.length - 1; i++){
        let cur = Number(levels[i])
        let next = Number(levels[i + 1])
        let delta = Math.abs(cur - next)
        if (delta > 3 || delta < 1) return false;
        if(increasing === 0){
            cur < next ? increasing = 1 : increasing = -1
        }
        else{
            if (increasing === 1 && cur > next) return false;
            if (increasing === -1 && cur < next) return false;
        }
    }
    return true;
}

fs.readFile('./Day2/input.txt', (err, data) => {
    let result = 0;
    if (err) throw err;
    const reports = data.toString().split('\n');
    reports.forEach(report => {
        if (check_report(report)) result++;
    });
    console.log(result)
})

function check_report_with_dampener(report:string):boolean{
    const levels = report.split(" ");
    for(let i = 0; i < levels.length; i++){
        let new_levels = levels.slice(0, i).concat(levels.slice(i + 1));
        let new_report = new_levels.join(" ")
        // console.log(new_report)
        if(check_report(new_report)) return true
    }
    return false
}
// Part 2
fs.readFile('./Day2/input.txt', (err, data) => {
    let result2 = 0;
    if (err) throw err;
    const reports = data.toString().split('\n');
    // forEach instead of map since don't modify the reports array
    reports.forEach(report => {
        if (check_report_with_dampener(report)) result2++;
    });
    console.log(result2)
})