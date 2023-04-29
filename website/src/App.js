import "./App.css";
import glasses from "./images/glasses.png";
import Button from "react-bootstrap/Button";
import singleglasses from "./images/singleglasses.png";
import React, { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import Card from "react-bootstrap/Card";

function App() {
  const onDrop = useCallback((acceptedFiles) => {
    console.log("File Uploaded");
    setIsFile(true);
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });
  const [isFile, setIsFile] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
        <div id="cardMain" className="flex flex-col gap-8 max-w-6xl">
          <div className="main-back">
            <div className="hero items-center p-10 rounded-3xl backdrop-blur-xl bg-black bg-opacity-50">
              <div className="flex flex-col text-left gap-2">
                <div className="text-7xl font-bold font-[OpenSans]">
                  SightSense
                </div>
                <div className="text-2xl font-bold italic">Your Third Eye</div>
              </div>
              <div className="rounded-2xl img-cont justify-end flex">
                <img
                  src={singleglasses}
                  className="rounded-3xl max-h-[300px]"
                  alt="logo"
                />
              </div>
            </div>
          </div>
          <hr></hr>
          <div className="main-back">
            <div
              id="card1"
              className="try-hero flex flex-col items-center p-10 rounded-3xl card-left gap-4 backdrop-blur-xl bg-black bg-opacity-50 "
            >
              <div className="flex flex-col text-desc text-center gap-2">
                <div className="text-5xl font-bold">What We Do</div>
              </div>
              <div className="rounded-2xl img-cont cardsCont">
                <Card className="card" style={{ width: "18rem" }}>
                  <Card.Img variant="top" src={glasses} />
                  <Card.Body>
                    <div className="text-black text-xl font-bold" >Image Captioning</div>
                    <div className="text-black text-base">
                      Some quick example text to build on the card title and
                      make up the bulk of the card's content.
                    </div>
                  </Card.Body>
                </Card>
                <Card style={{ width: "18rem" }}>
                  <Card.Img variant="top" src={glasses} />
                  <Card.Body>
                    <div className="text-black text-xl font-bold">Speech Recognition</div>
                    <div className="text-black text-base">
                      Some quick example text to build on the card title and
                      make up the bulk of the card's content.
                    </div>
                  </Card.Body>
                </Card>
                <Card style={{ width: "18rem" }}>
                  <Card.Img variant="top" src={glasses} />
                  <Card.Body>
                    <div className="text-black text-xl font-bold">Object Detection</div>
                    <div className="text-black text-base">
                      Some quick example text to build on the card title and
                      make up the bulk of the card's content.
                    </div>
                  </Card.Body>
                </Card>
              </div>
            </div>
          </div>
          <hr></hr>
          <div className="main-back">
            <div
              id="card2"
              className="child-hero items-center p-10 rounded-3xl card-left backdrop-blur-xl bg-black bg-opacity-50"
            >
              <div className="rounded-2xl img-cont justify-start flex">
                <img
                  src={glasses}
                  className="rounded-3xl max-h-[300px]"
                  alt="logo"
                />
              </div>
              <div className="flex flex-col text-desc text-right gap-2">
                <div className="text-5xl font-bold">How does it work?</div>
                <hr></hr>
                <div className="text-xl font-bold">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
                  quis mi maximus nibh euismod Sed quis Sed quis mi maximus nibh
                  euismod Sed quis mi maximus nibh euismod Sed quis mi maximus
                  nibh euismod Sed quis mi maximus nibh euismodmi maximus nibh
                  euismod Sed quis mi maximus nibh euismod.
                </div>
              </div>
            </div>
          </div>
          <hr></hr>
          <div className="main-back">
            <div
              id="card3"
              className="try-hero flex flex-col items-center p-10 rounded-3xl card-left gap-4 backdrop-blur-xl bg-black bg-opacity-50 "
            >
              <div className="flex flex-col text-desc text-center gap-2">
                <div className="text-5xl font-bold">View A Demo!</div>
              </div>
              <div className="fileDrop rounded-2xl img-cont justify-start flex backdrop-blur-xl bg-black bg-opacity-50">
                {!isFile ? (
                  <>
                    <div {...getRootProps()}>
                      <input {...getInputProps()} />
                      {isDragActive ? (
                        <div>Drop the files here ...</div>
                      ) : (
                        <div>
                          Drag or drop some files here, or click to select files
                        </div>
                      )}
                    </div>
                  </>
                ) : (
                  <div>File Loaded</div>
                )}
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
