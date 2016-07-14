google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data =  google.visualization.arrayToDataTable
            ([['X', 'Y', {'type': 'string', 'role': 'style'},{'type': 'string', 'role': 'tooltip'}],
              [{{econ}}, {{social}},'point { size: 10; shape-type: star; fill-color: #a52714; }','Your score'],
              [1, 9.8, null,'Adolf Hitler'],
              [8, 9, null,' Donald Trump'],
              [8, 8.5, null,'Jeb Bush'],
              [8.5, 8.5, null,' Ted Cruz'],
              [9, 7.5, null,' Marco Rubio'],
              [7, 4, null, 'Hillary Clinton'],
              [-2, 0, null, 'Bernie Sanders'],
              [-6, -4, null, 'Mahatma Gandhi'],
              [7, -2, null, 'Milton Friedman'],

        ]);

        var options = {
          legend: 'none',
          hAxis: { title:'Libertarian',minValue: -10, maxValue: 10 },
          vAxis: { title:'Left',minValue: -10, maxValue: 10 },
          title: "Authoritarian",
          curveType: 'function',
          pointSize: 7,
          dataOpacity: 0.3,
          fontSize: 20
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));
        chart.draw(data, options);
              movingAuthoritarian();


    }
    var movingAuthoritarian = function(){
    $('text:contains("Authoritarian")').attr("text-anchor", "middle")
    $('text:contains("Authoritarian")').attr("x", "400")
    $('text:contains("Authoritarian")').attr("font-weight", "")
    $('text:contains("Authoritarian")').attr("font-style", "italic")

    }