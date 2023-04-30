import "./App.css";
import glasses from "./images/glasses.png";
import Button from "react-bootstrap/Button";
import singleglasses from "./images/singleglasses.png";
import React, { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import Card from "react-bootstrap/Card";
import objDect from "./images/objDect.png";
import speechRec from "./images/speechRec.png";
import imgCap from "./images/imageCap.png";
import blind from "./images/blind.jpg";
import placeholder from "./images/placeholder.png";
import bottle from "./images/bottle.png"

function App() {
  const onDrop = useCallback((acceptedFiles) => {
    console.log("File Uploaded");
    setIsFile(true);
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });
  const [isFile, setIsFile] = useState(false);

  return (
    <div className="App">
      <header id="cardMain" className="App-header">
        <div className="flex flex-col gap-8 max-w-6xl">
          <div className="main-back">
            <div className="hero items-center p-10 rounded-3xl backdrop-blur-xl bg-black bg-opacity-50">
              <div className="flex flex-col text-left gap-2">
                <div className="text-7xl font-bold font-[OpenSans]">
                  SightSense
                </div>
                <div className="text-2xl font-bold italic">Your Third Eye - Empowering the visually impaired</div>
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
          <hr id="card1"></hr>
          <div className="main-back">
            <div className="try-hero flex flex-col items-center p-10 rounded-3xl card-left gap-4 backdrop-blur-xl bg-black bg-opacity-50 ">
              <div className="flex flex-col text-desc text-center gap-2">
                <div className="text-5xl font-bold">What Do We Do?</div>
              </div>
              <div className="rounded-2xl img-cont cardsCont">
                <Card className="card" style={{ width: "18rem" }}>
                  <Card.Img variant="top" src={imgCap} />
                  <Card.Body>
                    <div className="text-black text-xl font-bold">
                      Image Captioning
                    </div>
                    <div className="text-black text-base">
                      Our glasses automatically detect your surroundings and
                      describe them to you in detail.
                    </div>
                  </Card.Body>
                </Card>
                <Card style={{ width: "18rem" }}>
                  <Card.Img variant="top" src={speechRec} />
                  <Card.Body>
                    <div className="text-black text-xl font-bold">
                      Speech Recognition
                    </div>
                    <div className="text-black text-base">
                      Users can use voice commands to control the glasses and
                      its abilities, enhancing accessibility.
                    </div>
                  </Card.Body>
                </Card>
                <Card style={{ width: "18rem" }}>
                  <Card.Img variant="top" src={bottle} />
                  <Card.Body>
                    <div className="text-black text-xl font-bold">
                      Object Detection
                    </div>
                    <div className="text-black text-base">
                      The glasses perform object detection in real-time and
                      alert you of their presence.
                    </div>
                  </Card.Body>
                </Card>
              </div>
            </div>
          </div>
          <hr id="card2"></hr>
          <div className="main-back">
            <div className="child-hero items-center p-10 rounded-3xl card-right backdrop-blur-xl bg-black bg-opacity-50">
              <div className="flex flex-col text-desc  text-left gap-2">
                <div className="text-5xl font-bold">Who will this help?</div>
                <hr></hr>
                <div className="text-xl">
                  Visual impairment is a significant problem for millions of
                  people worldwide, limiting their independence and making
                  navigation challenging. Existing tools are often limited in
                  their capabilities and expensive. Our glasses provide an
                  affordable and unique solution, utilizing object detection,
                  voice commands, image captioning, and text-to-speech
                  functionality. This has the potential to enhance the
                  independence and quality of life for individuals with visual
                  impairments.
                </div>
              </div>
              <div className="rounded-2xl img-cont justify-end flex">
                <img
                  src={blind}
                  className="rounded-3xl max-h-[300px]"
                  alt="logo"
                />
              </div>
            </div>
          </div>
          <hr id="card3"></hr>
          <div className="main-back">
            <div className="child-hero items-center p-10 rounded-3xl card-left backdrop-blur-xl bg-black bg-opacity-50">
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
                <div className="text-xl">
                  Our product utilizes a Jetson Nano 4GB module, a Microsoft
                  webcam, a speaker, and normal sunglasses to perform real-time
                  object detection, image captioning, voice commands, and
                  text-to-speech functionality, all seamlessly integrated to aid
                  individuals with visual impairments in navigating their
                  surroundings with greater independence and autonomy.
                </div>
              </div>
            </div>
          </div>
          <hr id="card4"></hr>
          <div className="main-back">
            <div className="try-hero flex flex-col items-center p-10 rounded-3xl card-left gap-4 backdrop-blur-xl bg-black bg-opacity-50 ">
              <div className="flex flex-col text-desc text-center gap-2">
                <div className="text-5xl font-bold">View A Demo!</div>
              </div>
              <img src={placeholder} className="rounded-3xl max-h-[300px]" alt="logo" />
              {/* <div className="fileDrop rounded-2xl img-cont justify-start flex backdrop-blur-xl bg-black bg-opacity-50">
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
              </div> */}
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
