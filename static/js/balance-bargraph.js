var dataset = [];
var balance = function(d){
   return parseFloat(d.Balance);
};

var margin = {top: 20, right: 40, bottom: 20, left: 40};
var height = 650 - margin.top - margin.bottom;
var width = 1000 - margin.left - margin.right;
var svg = d3.select('#graphspace')
   .append('svg')
   .attr("height", height + margin.top + margin.bottom)
   .attr("width", width + margin.left + margin.right)
   .append("g")
   .attr("transform", 
      "translate(" + margin.left + "," + margin.top + ")");

var yscale = d3.scale.linear()
   .domain(d3.extent(dataset, balance))
   .rangeRound([height,0])
   .nice();

var xscale = d3.scale.ordinal()
   .domain(d3.range(dataset.length))
   .rangeBands([0,width],0.05)

var positiveColourScale = d3.scale.linear()
   .domain([0,d3.max(dataset, balance)])
   .rangeRound([150,0])
   .nice();
var negativeColourScale = d3.scale.linear()
   .domain([0,d3.min(dataset, balance)])
   .rangeRound([150,0])
   .nice();

var yaxis = d3.svg.axis()
   .scale(yscale)
   .orient("left");

svg.selectAll('rect')
   .data(dataset.reverse())
   .enter()
   .append('rect')
   .attr({
      x: function(d,i){
         return xscale(i);
      },
      y: function(d){
         return yscale(Math.max(0,balance(d)));
      },
      width: xscale.rangeBand(),
      height: function(d){
         return Math.abs(yscale(balance(d)) - yscale(0));
      },
      fill: function(d){
         if(balance(d) > 0){
            var amt = positiveColourScale(balance(d));
            return "rgb(" + amt + "," + amt + "," + amt + ")";
         } else {
            var amt = negativeColourScale(balance(d));
            return "rgb(255," + amt + "," + amt + ")";
         }
      }
   })
   .on("mouseover", function(d){
      var xPosition = parseFloat(d3.select(this).attr('x'))
         + xscale.rangeBand();
      var yPosition = parseFloat(d3.select(this).attr('y'))
         / 2 + height / 2;
      d3.select("#tooltip")
         .style("left", xPosition + "px")
         .style("top", yPosition + "px")
         .select("#value")
         .text(d.Amount);
      d3.select("#itemdesc").text(d.Description);
      d3.select("#tooltip").classed("hidden", false);
   })
   .on("mouseout", function(){
      d3.select("#tooltip").classed("hidden", true);
   });
svg.append("g")
   .attr("class", "axis")
   .call(yaxis);

d3.select("#fileinput").on("change", function(){
   var file = d3.event.target.files[0];
   if(file){
      var reader = new FileReader();
      reader.onloadend = function(evt){
         var dataUrl = evt.target.result;
         updateGraph(dataUrl);
      };
      reader.readAsDataURL(file);
   }
});

var updateGraph = function(rawdata){
   d3.csv(rawdata, function(dataset){
      var bars = svg.selectAll("rect").data(dataset.reverse());
      xscale.domain(d3.range(dataset.length));
      if(d3.min(dataset, balance) < 0){
         yscale.domain(d3.extent(dataset, balance));
      } else {
         yscale.domain([0,d3.max(dataset, balance)]);
      }
      svg.select('axis')
         .transition()
         .duration(1000)
         .call(yaxis);
      positiveColourScale.domain([0,d3.max(dataset, balance)]);
      negativeColourScale.domain([0,d3.min(dataset, balance)]);
      
      // Exit first
      bars.exit()
         .transition()
         .duration(1000)
         .style("opacity", 0)
         .remove();
      
      // Enter new bars
      bars.enter()
         .append("rect")
         .attr("x", width)
         .attr("y", function(d){
            return yscale(Math.max(0,balance(d)));
         })
         .on("mouseover", function(d){
            var xPosition = parseFloat(d3.select(this).attr('x'))
               + xscale.rangeBand();
            var yPosition = parseFloat(d3.select(this).attr('y'))
               / 2 + height / 2;
            d3.select("#tooltip")
               .style("left", xPosition + "px")
               .style("top", yPosition + "px")
               .select("#value")
               .text(d.Amount);
            d3.select("#itemdesc").text(d.Description);
            d3.select("#tooltip").classed("hidden", false);
         })
         .on("mouseout", function(){
            d3.select("#tooltip").classed("hidden", true);
         });

      // Update
      bars.transition()
         .duration(1000)
         .attr("y", function(d){
            return yscale(Math.max(0,balance(d)));
         })
         .attr("x", function(d,i){
            return xscale(i);
         })
         .attr("width", xscale.rangeBand())
         .attr("height", function(d){
            return Math.abs(yscale(balance(d)) - yscale(0));
         })
         .attr("fill", function(d){
            if(balance(d) > 0){
               var amt = positiveColourScale(balance(d));
               return "rgb(" + amt + "," + amt + "," + amt + ")";
            } else {
               var amt = negativeColourScale(balance(d));
               return "rgb(255," + amt + "," + amt + ")";
            }
         })

      svg.select(".axis").call(yaxis);
   });
};
