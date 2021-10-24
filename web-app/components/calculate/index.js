import { Space, Input, Alert } from "antd";
import { useState } from "react";
import calculateFactorial from "../../utils/calculate-factorial";

export default function CalculateComponent(){

    const [factorialResult, setFactorialResult] = useState(null)
    const [alert, setAlert] = useState(false)

    const handleInputChange = (event)=>{
        const {value} = event.target;

        if(value){

            // check letters are added
            const regExp = /^[0-9]*$/g;
            const isOnlyNumbers = regExp.test(value)
            if(!isOnlyNumbers){
                setAlert(true);
                return;
            }
            // check is negative number
            const isNegativeNumber = value < 0
            if(isNegativeNumber){
                setAlert(true);
                return;
            }

            return setFactorialResult(calculateFactorial(parseInt(value)));
        }

        setAlert(false);
        return setFactorialResult(null);
    }
    return (
        <Space direction="vertical">
            <Input onChange={handleInputChange}/>
                {factorialResult && 
                    <Alert message={factorialResult} type="success" />
                }
                {alert && <Alert message="Please enter a valid value!" type="error" />}
        </Space>
    )}