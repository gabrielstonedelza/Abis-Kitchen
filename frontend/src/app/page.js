 import Image from 'next/image'
import styles from './page.module.css'


import FoodLists from './foodlists'

export default function Home() {
  return (
    <main className={styles.main}>
      <FoodLists />
    </main>
  )
}
