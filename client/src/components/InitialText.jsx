import React from 'react'
import Robo from "../assets/robo.png"

const InitialText = () => {
  return (
    <div className='flex flex-col items-center justify-center h-full -mt-20'>
        <img src={Robo} alt="" className='h-40 grayscale-50 opacity-20'  />
        <p className='mt-2 font-semibold text-zinc-500'>Start Asking Questions!</p>
    </div>
  )
}

export default InitialText