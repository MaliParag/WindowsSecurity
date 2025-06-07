document.addEventListener('DOMContentLoaded', function() {
  // Create the first script element
  const script1 = document.createElement('script');
  script1.async = true;
  script1.src = 'https://www.googletagmanager.com/gtag/js?id=G-NZ3EC3JMH0';

  // Create the second script element
  const script2 = document.createElement('script');
  script2.innerHTML = `
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-NZ3EC3JMH0');
  `;

  // Append both script elements to the document's <head>
  document.head.appendChild(script1);
  document.head.appendChild(script2);
});
