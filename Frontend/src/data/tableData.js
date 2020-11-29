var rows = [
    ['Salaries', "Office", "Merchandise", "Legal", "Total"],
    [1,2,3,4,5],
    [11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35]
];

var colnames = [["Expenses"], ["Q1"], ["Q2"], ["Q3"], ["Q4"]];

export var data = {
    type: "table",

    header: {
        values: colnames,
        align: "center",
        line: {width: 1, color: 'black'},
        fill: {color: "grey"},
        font: {family:"Arial", size:12, color: "white"}
    },

    cells: {
        values: rows,
        align: "center",
        line: {color: "black", width: 1},
        font: {family:"Arial", size:11, color: ["black"]}
    }
}