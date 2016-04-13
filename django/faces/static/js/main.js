
// google.charts.load('current', {'packages':['corechart']});
//       google.charts.setOnLoadCallback(drawChart);
//       function drawChart() {
//         var data =  google.visualization.arrayToDataTable
//             ([['X', 'Y', {'type': 'string', 'role': 'style'},{'type': 'string', 'role': 'tooltip'}],
//               [{{econ}}, {{social}},'point { size: 18; shape-type: star; fill-color: #a52714; }','Your score'],
//               [6, 6, null,'hitler'],
//               [-2, -4, null,'bob the builder'],
              
              
//         ]);

//         var options = {
//           legend: 'none',
//           hAxis: { minValue: -10, maxValue: 10 },
//           vAxis: { minValue: -10, maxValue: 10 },

//           curveType: 'function',
//           pointSize: 7,
//           dataOpacity: 0.3
//         };

//         var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));
//         chart.draw(data, options);
//     }
// });


// // $("#submit").click(function(){

// // google.charts.load('current', {'packages':['corechart']});
// //       google.charts.setOnLoadCallback(drawChart);
// //       function drawChart() {
// //         var data = google.visualization.arrayToDataTable([
// //           ['Age', 'Weight'],
// //           [ {{econ}}, {{social}}],
          
// //         ]);

// //         var options = {
// //           title: 'Age vs. Weight comparison',
// //           hAxis: {title: 'Age', minValue: -10, maxValue: 15},
// //           vAxis: {title: 'Weight', minValue: -10, maxValue: 15},
// //           legend: 'none'
// //         };

// //         var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

// //         chart.draw(data, options);
// //       }
// //  });
// // $(".submit").on("click", function(event){
// // 	event.preventDefault();
// // 	console.log('did it work??')
// // 		$.ajax({
// // 			method: "POST",
// // 			url: "http://localhost:8000/submit",
// // 			success: function(result){
// // 			},
// // 			error: function(){console.log('not quite')
// // 			}
// // 		})
// // });

// // Dropzone.options.myDropzone = {

// //     // Prevents Dropzone from uploading dropped files immediately
// //     autoProcessQueue : false,

// //     init : function() {
// //         var submitButton = document.querySelector("#submit-all")
// //         myDropzone = this;

// //         submitButton.addEventListener("click", function() {
// //             myDropzone.processQueue();
// //             // Tell Dropzone to process all queued files.
// //         });

// //         // You might want to show the submit button only when
// //         // files are dropped here:
// //         this.on("addedfile", function() {
// //             // Show submit button here and/or inform user to click it.
// //         });

// //     }
// // };
