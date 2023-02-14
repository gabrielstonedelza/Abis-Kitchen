export const load = async ({ fetch }) => {
    const res = await fetch('http://127.0.0.1:8000/all-food');
    const data = res.json();

    return {
        data
    };
};