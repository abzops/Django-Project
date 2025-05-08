document.addEventListener('DOMContentLoaded', function() {
  // Sidebar Toggle
  const sidebar = document.querySelector('.sidebar');
  const sidebarToggle = document.querySelector('.sidebar-toggle');
  
  sidebarToggle.addEventListener('click', function() {
    sidebar.classList.toggle('active');
  });
  
  // Theme Toggle
  const themeToggle = document.querySelector('.theme-toggle');
  const themeIcon = themeToggle.querySelector('i');
  
  themeToggle.addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    
    if (document.body.classList.contains('dark-mode')) {
      themeIcon.classList.remove('ri-moon-line');
      themeIcon.classList.add('ri-sun-line');
    } else {
      themeIcon.classList.remove('ri-sun-line');
      themeIcon.classList.add('ri-moon-line');
    }
  });
  
  // Complete Project Button
  const completeButtons = document.querySelectorAll('.btn-complete');
  
  completeButtons.forEach(button => {
    button.addEventListener('click', function() {
      const projectId = this.getAttribute('data-id');
      const projectCard = this.closest('.project-card');
      
      if (!confirm('Mark this project as complete?')) return;
      
      // Add loading state
      this.innerHTML = '<i class="ri-loader-4-line spin"></i> Processing';
      this.disabled = true;
      
      // Animate card
      projectCard.style.transform = 'scale(0.98)';
      projectCard.style.opacity = '0.9';
      
      // Simulate API call
      setTimeout(() => {
        // Add completion animation
        projectCard.style.transition = 'all 0.6s ease';
        projectCard.style.transform = 'translateY(-20px)';
        projectCard.style.opacity = '0';
        
        // Remove card after animation
        setTimeout(() => {
          projectCard.remove();
          
          // Check if no projects left
          if (document.querySelectorAll('.project-card').length === 0) {
            showEmptyState();
          }
        }, 600);
      }, 1000);
    });
  });
  
  // Show empty state if no projects
  function showEmptyState() {
    const projectsGrid = document.querySelector('.projects-grid');
    const emptyState = document.createElement('div');
    emptyState.className = 'empty-state';
    emptyState.innerHTML = `
      <div class="empty-icon">
        <i class="ri-folder-open-line"></i>
      </div>
      <h3>No Projects Found</h3>
      <p>Get started by creating your first project</p>
      <button class="btn-primary">
        <i class="ri-add-line"></i> Add New Project
      </button>
    `;
    
    projectsGrid.appendChild(emptyState);
  }
  
  // Add spin animation to loader icons
  const style = document.createElement('style');
  style.innerHTML = `
    @keyframes spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    .spin {
      animation: spin 1s linear infinite;
    }
  `;
  document.head.appendChild(style);
});