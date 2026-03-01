fetch("../output/ranking.json")
  .then(res => res.json())
  .then(data => {
    const ul = document.getElementById("ranking");
    data.forEach(item => {
      const li = document.createElement("li");
      li.innerText = item[0] + " Score: " + item[1].toFixed(2);
      ul.appendChild(li);
    });
  });

fetch("../output/portfolio_stats.json")
  .then(res => res.json())
  .then(data => {
    document.getElementById("stats").innerText = JSON.stringify(data, null, 2);
  });
