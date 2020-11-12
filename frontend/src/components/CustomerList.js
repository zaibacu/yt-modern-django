import React from "react"
import { useState, useEffect } from "react";
import { loadCustomers } from "../actions";

export default () => {
    const [customers, setCustomers] = useState([]);
    const [selectedCustomer, setSelectedCustomer] = useState("");

    useEffect(() => {
        loadCustomers().then(data => setCustomers(data))
    }, []);

    const renderCustomer = (c) => {
        console.log(c);
        return (<tr key={c.id} onClick={() => setSelectedCustomer(c)}>
            <td>{c.name}</td>
            <td>{c.category.name}</td>
            <td>{c.country}</td>
            <td>{c.address}</td>
            <td>{c.phone}</td>
        </tr>);
    };

    const renderEvent = (e) => {
        return (
            <li className="collection-item" key={e.id}>
                {e.comment}
                <i className="secondary-content">[{e.created}]</i>
            </li>);
    }

    return (
        <div>
            <table className="striped highlight">
                <thead>
                    <tr>
                        <th>Pavadinimas</th>
                        <th>Kategorija</th>
                        <th>Šalis</th>
                        <th>Adresas</th>
                        <th>Tel. Numeris</th>
                    </tr>
                </thead>
                <tbody>
                {customers.length == 0 ? (<tr><td colSpan={5}>"Nėra klientų"</td></tr>) : customers.map(renderCustomer)}
                </tbody>
            </table>
            <div>
                <h5>Įvykiai</h5>
                { selectedCustomer == "" ? "Klientas nepasirinktas" : (<ul className="collection">{selectedCustomer.event_set.map(renderEvent)}</ul>)}
            </div>
        </div>);
}