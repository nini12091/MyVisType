// set the dimensions and margins of the graph
var margin = {top: 30, right: 70, bottom: 70, left: 70},
  width = 600 - margin.left - margin.right,
  height = 470 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg1 = d3.select("#type_bar")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Parse the Data
d3.csv("https://raw.githubusercontent.com/nini12091/myvistype_data/main/Multi_set_Bar_Chart1(type).csv", 

function(data) {

  // List of subgroups = header of the csv files = soil condition here
  var subgroups = data.columns.slice(1)

  // List of groups = species here = value of the first column called group -> I show them on the X axis
  var countrys = d3.map(data, function(d){return(d.country)}).keys()

// Add X axis
var x = d3.scaleBand()
    .domain(countrys)
    .range([0, width])
    .padding([0.1])
svg1.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x).tickSizeOuter(0))
  .attr("font-size", "14px");

// Add Y axis
var y = d3.scaleLinear()
  .domain([0, 320])
  .range([ height, 0 ]);
svg1.append("g")
  .call(d3.axisLeft(y))
  .attr("font-size", "14px");

// Another scale for subgroup position?
var xSubgroup = d3.scaleBand()
    .domain(subgroups)
    .range([0, x.bandwidth()])
    .padding([0.05])

// gridlines in y axis function
function make_y_gridlines() {		
    return d3.axisLeft(y)
        .ticks(25)
}

// add the Y gridlines
svg1.append("g")			
  .attr("class", "grid")
  .attr('fill','none')
  .attr('stroke', '#DCDCDC')
  .attr('stroke-width',0.1)
  .attr('shape-rendering','crispEdges')
  .call(make_y_gridlines()
      .tickSize(-width)
      .tickFormat("")
  )
// Add X axis name
svg1.append("text")
  .attr("x", width - 70)
  .attr("y", margin.top - 38)
  .attr("font-size", "12px")
  .text("(단위 : 명 / 인구 10만명)");

// color palette = one color per subgroup
var color = d3.scaleOrdinal()
    .domain(subgroups)
    .range(['#CC79A7','#E69F00','#009E73','#0072B2'])

// 색상 정보
var subgroupitem = svg1.selectAll(".subgroupitem")
  .data(data.columns.slice(1).reverse())
  .enter().append("g")
        .attr("class", "subgroupitem")
        .attr("transform", function(d, i) { return "translate(0," + i * 25 + ")"; });

// 색상 모형
subgroupitem.append("rect")
  .attr("x", width - 15)
  .attr("y", 4)
  .attr("width", 15)
  .attr("height", 15)
  .style("fill", color );

//색상 text
subgroupitem.append("text")
  .attr("x", width + 5)
  .attr("y", 10)
  .attr("font-size", "13px")
  .attr("dy", ".55em")
  .style("text-anchor", "start")
  .text(function(d) { return d; });

// Add X axis name
svg1.append("text")
  .attr("y", margin.bottom + 330)
  .attr("x",(width / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("국가명");

// Add Y axis name
svg1.append("text")
  .attr('transform','rotate(-90)')
  .attr("y", 20 - margin.left)
  .attr("x",0 - (height / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("사망자 수(명)");

  // Show the bars
svg1.append("g")
    .selectAll("g")
    // Enter in data = loop group per group
    .data(data)
    .enter()
    .append("g")
      .attr("transform", function(d) { return "translate(" + x(d.country) + ",0)"; })
    .selectAll("rect")
    .data(function(d) { return subgroups.map(function(key) { return {key: key, value: d[key]}; }); })
    .enter().append("rect")
      .attr("x", function(d) { return xSubgroup(d.key); })
      .attr("y", function(d) { return y(d.value); })
      .attr("width", xSubgroup.bandwidth())
      .attr("height", function(d) { return height - y(d.value); })
      .attr("fill", function(d) { return color(d.key); });

})