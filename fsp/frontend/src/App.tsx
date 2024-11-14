import React from 'react'
import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'


function App() {
    const [foods, setFoods] = useState<FoodItem[]>([])

    interface FoodItem {
        name: string;
        price: number;
        photo_url: string;
        stock: number;
    }

    useEffect(() => {
        const foodsListUrl = 'http://localhost:8000/menu/'
        axios.get<FoodItem[]>(foodsListUrl)
            .then(response => setFoods(response.data))
    }, [])

    return (
        <>
            <div> Hi
            </div>
        </>
    )
}

export default App