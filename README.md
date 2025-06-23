


## How It Works

* Scans the provided folder.
* Filters files by the given extension.
* Moves matching files into a new folder named `<extension>_files`.

---

## Example Folder Structure Before

```
Downloads/
├── video1.mp4
├── video2.mp4
├── document.pdf
├── image.jpg
```

## Example Folder Structure After

```
Downloads/
├── document.pdf
├── image.jpg
├── mp4_files/
│   ├── video1.mp4
│   └── video2.mp4
```

---

## Notes

* You can pass any file extension, like `mp4`, `jpg`, `pdf`, etc.
* Files with both uppercase and lowercase extensions will be correctly classified.


