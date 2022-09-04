import { UploadTypeProps } from '../../../objects/UploadType';
import './UploadTypeButton.css';

function UploadTypeButton({ name, icon }: UploadTypeProps) {
    return (
        <div className="UploadTypeButton">
            <button>
                <img src={icon} alt="Upload" />
                {name}
            </button>
        </div>
    );
}

export default UploadTypeButton;