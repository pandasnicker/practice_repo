
createChart();

async function createChart() {
    const dta = await getData();
    const ctx = document.getElementById('chart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: dta[0],
            datasets: [{
                label: 'PIA Approvals',
                data: dta[1],
                backgroundColor: ['rgba(100, 150, 52, .5)'],
                borderColor: ['rgba(255, 99, 132, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            mantainAspectRatio: false,
        }
    });

    const cs = document.getElementsByTagName('canvas');
    cs.height = 500;
    cs.width = 300;
}

async function getData() {
    const resp = await fetch('inp.csv');
    const dta = await resp.text();
    const x = [];
    const y = [];

    const table = dta.split('\r\n').slice(1);
    table.forEach(row => {
        if (row.length != 0) {
            const columns = row.split(',');
            x.push(columns[0]);
            y.push(columns[3]);
        }
    })
    return [x, y];
}
