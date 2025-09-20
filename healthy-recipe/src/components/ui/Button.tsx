
interface ButtonProps {
    title: string;
}
export const Button = (props: ButtonProps) => {
    return (
<button className="px-8 py-4 text-white bg-neutral-900 border rounded-xl">{props.title}</button>
    )
}