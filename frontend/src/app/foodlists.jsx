import React from 'react'

const fetchFoodList = async() => {
    const res = await fetch("http://127.0.0.1:8000/all-food/",{cache: "no-cache"})
    const data = res.json()
    console.log(data)
    return data

}
 
async function FoodLists () {
    const foodlists = await fetchFoodList()
    
  return (
    <div>FoodLists</div>
  )
}

export default FoodLists