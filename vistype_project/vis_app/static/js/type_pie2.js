// set the dimensions and margins of the graph
var margin_pie1 = 30
width_pie1 = 200
height_pie1 = 200

var radius = Math.min(width_pie1, height_pie1) / 2 - margin_pie1

var svg5 = d3.select("#type_pie2")
.append("svg")
.attr("width", width_pie1)
.attr("height", height_pie1)
.append("g")
.attr("transform", "translate(" + width_pie1 / 2 + "," + height_pie1 / 2 + ")");

var color = d3.scaleOrdinal(['#0072B2','#009E73','#E69F00','#CC79A7']);

var pie = d3.pie()
.sort(null)
.value(function(d) { return d.percent; });

var path = d3.arc()
.outerRadius(radius - 10)
.innerRadius(0);

var label = d3.arc()
.outerRadius(radius + 20)
.innerRadius(radius);

d3.csv("https://raw.githubusercontent.com/nini12091/myvistype_data/main/Pie_Chart(type_%EB%8F%85%EC%9D%BC).csv", 

function(d) {

d.percent = +d.percent;
return d;
}, function(error, data){
if (error) throw error;

var arc2 = svg5.selectAll(".arc")
  .data(pie(data))
  .enter().append("g")
    .attr("class", "arc");

arc2.append("path")
    .attr("d", path)
    .attr("fill", function(d) { return color(d.data.질병); })

arc2.append("text")
    .attr("transform", function(d) { return "translate(" + label.centroid(d) + ")"; })
    .attr("dx", "-1em")
    .attr("font-size", "13px")
    .attr("dy", "0.5em")
    .text(function(d) { return d.data.질병; });
  
  
});