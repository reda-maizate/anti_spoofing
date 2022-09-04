import './UploadFromFile.css';

function UploadFromFile() {
    return (
        <div className="UploadFromFile">
            <input type="file" id="file" accept="image/*" required placeholder='Choose a picture from your computer'/>
        </div>
    );
}

export default UploadFromFile;