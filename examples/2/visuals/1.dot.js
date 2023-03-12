info.dot = `
graph {
bgcolor=transparent
node [style=filled, color=aliceblue]
1 [label="1"]
2 [label="2"]
3 [label="3"]
4 [label="4"]
5 [label="5"]
1 -- 2
1 -- 4
2 -- 3
2 -- 4
3 -- 4
4 -- 5
}
`
