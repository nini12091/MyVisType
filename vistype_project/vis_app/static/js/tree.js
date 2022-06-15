// set the dimensions and margins of the graph
var margin = {top: 10, right: 10, bottom: 30, left: 10},
  width = 700 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#tree")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
    "translate(" + margin.left + "," + margin.top + ")");

// read json data
d3.json("https://raw.githubusercontent.com/nini12091/myvistype_data/main/Treemap(test).json", function(data) {

// Give the data to this cluster layout:
var root = d3.hierarchy(data).sum(function(d){ return d.value}) 

// Then d3.treemap computes the position of each element of the hierarchy
d3.treemap()
.size([width, height])
.paddingTop(18)
.paddingRight(3)
.paddingLeft(3)
.paddingInner(1.5)    
(root)

// prepare a color scale
var color = d3.scaleOrdinal()
.domain(["육류","어패류", "곡물류", "유제품류"])
.range(['#CC79A7','#E69F00','#009E73','#0072B2'])

// And a opacity scale
var opacity = d3.scaleLinear()
.domain([0, 50])
.range([.3,3])  

// use this information to add rectangles:
svg
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
svg
.selectAll("text")
.data(root.leaves())
.enter()
.append("text")
.attr("x", function(d){ return d.x0+5})    // +10 to adjust position (more right)
.attr("y", function(d){ return d.y0+17})    // +20 to adjust position (lower)
.text(function(d){ return d.data.name })
.attr("font-size", "14px")
.attr("fill", "black")

// Add title for the 6 groups
svg
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

})