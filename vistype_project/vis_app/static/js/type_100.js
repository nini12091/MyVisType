// set the dimensions and margins of the graph
var margin_100 = {top: 30, right: 70, bottom: 70, left: 70},
  width_100 = 500 - margin_100.left - margin_100.right,
  height_100 = 330 - margin_100.top - margin_100.bottom;

// append the svg object to the body of the page
var svg10 = d3.select("#type_100")
.append("svg")
.attr("width", width_100 + margin_100.left + margin_100.right)
.attr("height", height_100 + margin_100.top + margin_100.bottom)
.append("g")
.attr("transform",
      "translate(" + margin_100.left + "," + margin_100.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/myvistype_data/main/100%25_Stacked_Bar_Chart2(type).csv", 

function(data) {

var subgroups = data.columns.slice(1)

var countrys = d3.map(data, function(d){return(d.country)}).keys()

// Add X axis
var x = d3.scaleBand()
    .domain(countrys)
    .range([0, width_100])
    .padding([0.1])
svg10.append("g")
  .attr("transform", "translate(0," + height_100 + ")")
  .call(d3.axisBottom(x).tickSizeOuter(0))
  .attr("font-size", "14px");

// Add Y axis
var y = d3.scaleLinear()
  .domain([0, 100])
  .range([ height_100, 0 ]);
svg10.append("g")
  .call(d3.axisLeft(y))
  .attr("font-size", "14px");

// gridlines in y axis function
function make_y_gridlines() {		
    return d3.axisLeft(y)
        .ticks(20)
}

// add the Y gridlines
svg10.append("g")			
  .attr("class", "grid")
  .attr('fill','none')
  .attr('stroke', '#DCDCDC')
  .attr('stroke-width',0.1)
  .attr('shape-rendering','crispEdges')
  .call(make_y_gridlines()
      .tickSize(-width_100)
      .tickFormat("")
  )

// color palette = one color per subgroup
var color = d3.scaleOrdinal()
  .domain(subgroups)
  .range(['#CC79A7','#E69F00','#009E73','#0072B2'])

// Normalize the data -> sum of each group must be 100!
console.log(data)
  dataNormalized = []
  data.forEach(function(d){
    // Compute the total
    tot = 0
    for (i in subgroups){ name=subgroups[i] ; tot += +d[name] }
    // Now normalize
    for (i in subgroups){ name=subgroups[i] ; d[name] = d[name] / tot * 100}
  })

//stack the data? --> stack per subgroup
var stackedData = d3.stack()
  .keys(subgroups)
  (data)

// 색상 정보
var subgroupitem = svg10.selectAll(".subgroupitem")
  .data(data.columns.slice(1).reverse())
  .enter().append("g")
        .attr("class", "subgroupitem")
        .attr("transform", function(d, i) { return "translate(0," + i * 25 + ")"; });

// 색상 모형
subgroupitem.append("rect")
  .attr("x", width_100 - 2)
  .attr("y", 4)
  .attr("width", 15)
  .attr("height", 15)
  .style("fill", color );

//색상 text
subgroupitem.append("text")
  .attr("x", width_100 + 17)
  .attr("y", 10)
  .attr("font-size", "13px")
  .attr("dy", ".55em")
  .style("text-anchor", "start")
  .text(function(d) { return d; });

// Add X axis name
svg10.append("text")
  .attr("x", width_100 - 70)
  .attr("y", margin_100.top - 38)
  .attr("font-size", "12px")
  .text("(단위 : 명 / 인구 10만명)");

// Add X axis name
svg10.append("text")
  .attr("y", margin_100.bottom + 190)
  .attr("x",(width_100 / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("국가명");

// Add Y axis name
svg10.append("text")
  .attr('transform','rotate(-90)')
  .attr("y", 20 - margin_100.left)
  .attr("x",0 - (height_100 / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("사망 수");

// Show the bars
svg10.append("g")
  .selectAll("g")
  // Enter in the stack data = loop key per key = group per group
  .data(stackedData)
  .enter().append("g")
    .attr("fill", function(d) { return color(d.key); })
    .selectAll("rect")
    // enter a second time = loop subgroup per subgroup to add all rectangles
    .data(function(d) { return d; })
    .enter().append("rect")
      .attr("x", function(d) { return x(d.data.country); })
      .attr("y", function(d) { return y(d[1]); })
      .attr("height", function(d) { return y(d[0]) - y(d[1]); })
      .attr("width", x.bandwidth())

})