import 'antd/dist/antd.css';
import {Result, Button} from "antd"
import MathSvg from '../components/svg/math';
import CalculateComponent from '../components/calculate';

export default function HomePage(){


    return <Result
                icon={<MathSvg/>}
                title="Please enter a number to calculate Factorial."
                extra={<CalculateComponent/>}
            />
}