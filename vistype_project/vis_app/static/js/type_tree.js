// set the dimensions and margins of the graph
var margin_tree = {top: 0, right: 10, bottom: 30, left: 0},
  width_tree = 670 - margin_tree.left - margin_tree.right,
  height_tree = 470 - margin_tree.top - margin_tree.bottom;

// append the svg object to the body of the page
var svg2 = d3.select("#type_tree")
.append("svg")
.attr("width", width_tree + margin_tree.left + margin_tree.right)
.attr("height", height_tree + margin_tree.top + margin_tree.bottom)
.append("g")
.attr("transform",
    "translate(" + margin_tree.left + "," + margin_tree.top + ")");

// read json data
d3.json("https://raw.githubusercontent.com/nini12091/myvistype_data/main/Treemap(type).json", function(data) {

// Give the data to this cluster layout:
var root = d3.hierarchy(data).sum(function(d){ return d.value}) 

// Then d3.treemap computes the position of each element of the hierarchy
d3.treemap()
.size([width_tree, height_tree])
.paddingTop(18)
.paddingRight(3)
.paddingLeft(3)
.paddingInner(1.5)    
(root)

// prepare a color scale
var color = d3.scaleOrdinal()
.domain(["대한민국","미국", "일본", "독일", "영국"])
.range(['#0072B2','#009E73','#D55E00','#CC79A7','#E69F00'])

// And a opacity scale
var opacity = d3.scaleLinear()
.domain([0, 50])
.range([.3,3])  

// use this information to add rectangles:
svg2
.selectAll("rect")
.data(root.leaves())
.enter()
.append("rect")
.attr('x', function (d) { return d.x0; })
.attr('y', function (d) { return d.y0; })
.attr('width', function (d) { return d.x1 - d.x0 - 3; })
.attr('height', function (d) { return d.y1 - d.y0 - 3; })
.style("stroke", "white")
.style("fill", function(d){ return color(d.parent.data.name)} )
.style("opacity", function(d){ return opacity(d.data.value)})


// and to add the text labels
svg2
.selectAll("text")
.data(root.leaves())
.enter()
.append("text")
.attr("x", function(d){ return d.x0+5})    // +10 to adjust position (more right)
.attr("y", function(d){ return d.y0+17})    // +20 to adjust position (lower)
.text(function(d){ return d.data.name })
.attr("font-size", "14px")
.attr("fill", "black")

// and to add the text labels
svg2
.selectAll("vals")
.data(root.leaves())
.enter()
.append("text")
.attr("x", function(d){ return d.x0+5})    // +10 to adjust position (more right)
.attr("y", function(d){ return d.y0+30})    // +20 to adjust position (lower)
.text(function(d){ return d.data.value + '명'})
.attr("font-size", "13px")
.attr("fill", "black")

// Add title for the 6 groups
svg2
.selectAll("titles")
.data(root.descendants().filter(function(d){return d.depth==1}))
.enter()
.append("text")
.attr("x", function(d){ return d.x0+5})
.attr("y", function(d){ return d.y0+13})
.text(function(d){ return d.data.name })
.attr("fill",  function(d){ return color(d.data.name)} )
.attr("font-size", "17px")
.attr("fill", "black")

// // Add title for the 6 groups
// svg2
// .append("text")
// .attr("x", 7)
// .attr("y", 10)    
// .text("각 국가의 사망원인별 사망 수")
// .attr("font-size", "20px")
// .attr("fill",  "black" )
// .style("font-weight", "bold")

})