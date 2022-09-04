import UploadTypeButton from "./atoms/UploadTypeButton";
import ChooseUploadType from "./molecules/ChooseUploadType";
import UploadFromCamera from "./molecules/UploadFromCamera";
import UploadFromFile from "./atoms/UploadFromFile";

function UploadPicture() {
    return (
        <div className="UploadPicture">
            <ChooseUploadType />
            <UploadFromFile />
            <UploadFromCamera />
        </div>
    );
}

export default UploadPicture;