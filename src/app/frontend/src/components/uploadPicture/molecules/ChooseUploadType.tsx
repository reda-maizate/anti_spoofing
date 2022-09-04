import { UploadTypeProps } from "../../../objects/UploadType";
import UploadTypeButton from "../atoms/UploadTypeButton";
import './ChooseUploadType.css';

const FileUpload: UploadTypeProps = {
    name: "File",
    icon: "https://img.icons8.com/material-outlined/344/file.png"
}

const CameraUpload: UploadTypeProps = {
    name: "Camera",
    icon: "https://img.icons8.com/material-outlined/344/compact-camera--v2.png"
}


function ChooseUploadType() {
    return (
        <div className="ChooseUploadType">
            <UploadTypeButton name={FileUpload.name} icon={FileUpload.icon} />
            <UploadTypeButton name={CameraUpload.name} icon={CameraUpload.icon} />
        </div>
    );
}

export default ChooseUploadType;