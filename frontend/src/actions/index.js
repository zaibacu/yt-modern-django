export const loadCustomers = async () => {
    const url = "/api/customers/";
    const authToken = window.ACCESS_TOKEN;

    const conf = {
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Token ${authToken}`
        }
    };

    return await fetch(url, conf).then(resp => resp.json());
};