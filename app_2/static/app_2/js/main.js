$("#get-company").submit("click", (e) => {
    e.preventDefault();
    const company_id = $('select').find(':selected').data('id')
    const company_name = $('select').find(':selected').val()
    const start_date = $('#start-date').val()
    const end_date = $('#end-date').val()
    const table = $('.table')

    const data = {
        'company_id': company_id,
        'start_date': start_date,
        'end_date': end_date,
    }

    $.ajax({
        type: 'GET',
        url: '/ajax/get_prices',
        data: data,
        dataType: 'json',
        success: function ({data}) {
            console.log(data)
            table.empty();
            let newTable = `
                <table class="table table-striped table-bordered table-hover">
                    <thead class="thead-dark">
                        <tr key>
                            <th scope="col">Date</th>
                            <th scope="col">Price</th>
                        </tr>
                    </thead>
                    <tbody>`

            if (data !== undefined) {
                const data_json =  JSON.parse(data)
                console.log('nie pusto')
                data_json.map(data => {
                    newTable += `
                        <tr>
                            <td>${data.fields.date}</td>
                            <td>${data.fields.price}</td>
                        </tr>`
                })
            } else {
                console.log('pusto')
                newTable += `
                        <tr>
                            <td>None data</td>
                        </tr>`
            }

            newTable += `
                </tbody>
            </table>
            `
            table.append(`<h3>${company_name}</h3>`, newTable)
        },
        error: (response) => {
            alert("The request failed");
        },
    })
});
