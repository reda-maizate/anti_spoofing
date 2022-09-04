function UploadFromCamera() {
    return (
        <div className="UploadFromCamera">
            <input type="file" id="file" accept="image/*" />
            <label htmlFor="file">Take a picture</label>
        </div>
    );
}

export default UploadFromCamera;