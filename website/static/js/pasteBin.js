const notesContainer = document.getElementById('notesContainer');
const addNoteBtn = document.getElementById('addNoteBtn');

addNoteBtn.addEventListener('click', () => {
  const note = createNote();
  notesContainer.appendChild(note);
});

document.addEventListener('DOMContentLoaded', () => {
    const note = createNote();
    notesContainer.appendChild(note);
  });

  function createNote() {
    const noteContainer = document.createElement('div');
    noteContainer.classList.add('note', 'is-flex');
  
    const noteTextarea = document.createElement('textarea');
    noteTextarea.classList.add('textarea');
    noteTextarea.draggable = true;
  
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.classList.add('button', 'is-danger', 'is-small', 'ml-2');
    deleteBtn.addEventListener('click', () => {
      notesContainer.removeChild(noteContainer);
    });
  
    const saveBtn = document.createElement('button');
    saveBtn.textContent = 'Save';
    saveBtn.classList.add('button', 'is-success', 'is-small', 'ml-2');
    saveBtn.addEventListener('click', () => {
      // Add save functionality here
      // For now, we'll just log the textarea value
      console.log(noteTextarea.value);
    });
  
    noteContainer.appendChild(noteTextarea);
    noteContainer.appendChild(deleteBtn);
    noteContainer.appendChild(saveBtn);
  
    noteContainer.addEventListener('dragover', (e) => {
      e.preventDefault();
      const draggingNote = document.querySelector('.is-dragging');
      const afterElement = getDragAfterElement(notesContainer, e.clientY);
      if (afterElement == null) {
        notesContainer.appendChild(draggingNote);
      } else {
        notesContainer.insertBefore(draggingNote, afterElement);
      }
    });
  
    return noteContainer;
  }
  
  function getDragAfterElement(container, y) {
    const draggableElements = [...container.querySelectorAll('.note:not(.is-dragging)')];
    return draggableElements.reduce((closest, child) => {
      const box = child.getBoundingClientRect();
      const offset = y - box.top - box.height / 2;
      if (offset < 0 && offset > closest.offset) {
        return { offset: offset, element: child };
      } else {
        return closest;
      }
    }, { offset: Number.NEGATIVE_INFINITY }).element;
  }