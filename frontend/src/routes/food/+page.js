export const load = async ({ fetch }) =>{
    const res = await fetch('http://127.0.0.1:8000/all-food',{
        headers: {
            'content-type': 'application/json',
            accept: 'application/json'
        }
    });
    const food_data = res.json();
    return {
        food_data
    };
}